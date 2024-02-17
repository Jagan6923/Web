from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import FormData,FieldData

def home(request):
    
    return render (request,'home.html')

@csrf_exempt
def submit_form_data(request):
    if request.method == 'POST':
        # Initialize an empty list to store form data
        form_data_list = []
        items_list = list(request.POST.items())

        for (key1, value1), (key2, value2) in zip(items_list[::2], items_list[1::2]):
            if key1.startswith('form') and key2.endswith('path'):
                form_key= key1
                forms_name = value1 
                Rediretpath_name= value2
             
                form_data = {
                    'form_key': form_key,
                    'Rediretpath_name': Rediretpath_name,
                    'forms_name': forms_name
                }

                form_data_list.append(form_data)

        for form_data in form_data_list:
            FormData.objects.create(**form_data)

 
        return JsonResponse({'success': True})


@csrf_exempt
def submit_field_data(request):
    if request.method == 'POST':
        # Initialize an empty list to store form data
        form_data_list = []

        items_list = list(request.POST.items())
        for (key1, value1), (key2, value2) in zip(items_list[::2], items_list[1::2]):
            if 'field' in key1 and 'selection' in key2:
                field_key = key1
                field_value = value1 
                selection_value = value2
                
                # Extract required and readable checkbox values
                required = 'required' in field_key
                readable = 'readable' in field_key
                
                # Remove checkbox indicators from field key
                field_key = field_key.split('|')[0]
                
                form_data = {
                    'field_key': field_key,
                    'field_value': field_value,
                    'selection_value': selection_value,
                    'required': required,
                    'readable': readable,
                }
               
                form_data_list.append(form_data)

        for form_data in form_data_list:
            FieldData.objects.create(**form_data)

        return JsonResponse({'success': True})
