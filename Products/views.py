from .models import AllProducts, RegularFit, RelaxedFit

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RelaxedFitSerializer, RegularFitSerializer


@api_view(['GET'])
def update_records_db(request):

    product_specifications = AllProducts.objects.all().values('product_specifications')
    relaxed_count = 0
    regular_count = 0
    for specification in product_specifications:
        product_specification = specification.get('product_specifications', "")
        if product_specification and isinstance(product_specification, dict):
            for keys, values_list in product_specification.items():
                if isinstance(values_list, list):
                    fit_flag = False
                    relaxed_flag = False
                    regular_flag = False
                    fabric_flag = False
                    ideal_for_flag = False
                    final_dict = dict()
                    for dicts in values_list:
                        for x, y in dicts.items():
                            # print(x, " : ", y)
                            if y.lower() == "fit":
                                fit_flag = True
                            elif "regular" in y.lower() and fit_flag:
                                regular_flag = True
                                fit_flag = False
                            elif "relaxed" in y.lower() and fit_flag:
                                relaxed_flag = True
                                fit_flag = False
                            elif y.lower() == "fabric":
                                fabric_flag = True
                            elif y.lower() == "ideal for":
                                ideal_for_flag = True
                            elif fabric_flag and x.lower() == "value":
                                final_dict['fabric'] = y
                                fabric_flag = False
                            elif ideal_for_flag and x.lower() == "value":
                                final_dict['ideal_for'] = y
                                ideal_for_flag = False

                    if relaxed_flag:
                        RelaxedFit.objects.create(fabric=final_dict.get('fabric', ""), ideal_for=final_dict.get('ideal_for', ""))
                        relaxed_count += 1
                    elif regular_flag:
                        RegularFit.objects.create(fabric=final_dict.get('fabric', ""), ideal_for=final_dict.get('ideal_for', ""))
                        regular_count += 1
    return Response({"message": "Success"})


@api_view(['GET'])
def get_fit_result(request):
    type_of_fit = request.query_params.get('type_of_fit', '')

    if type_of_fit.lower() == 'relaxed':
        rel_obj = RelaxedFit.objects.all()
        serializer_data = RelaxedFitSerializer(rel_obj, many=True)
    elif type_of_fit.lower() == 'regular':
        reg_obj = RegularFit.objects.all()
        serializer_data = RegularFitSerializer(reg_obj, many=True)
    else:
        return Response({'error': 'Invalid type_of_fit parameter'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"data": serializer_data.data}, status=status.HTTP_200_OK)
