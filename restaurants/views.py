from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" :
    		[
    			{
    				"restaurant_name" : "Flikory",
    				"food_type" : "Italic food"
    			},
    			{
    				"restaurant_name" : "Dip in Dip",
    				"food_type" : "Coffee"
    			},
    			{
    				"restaurant_name" : "Paskin Robens",
    				"food_type" : "Ice cream"
    			}

    		]

    	}

    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object" : {
                    "restaurant_name" : "Flikory",
                    "food_type" : "Italic food"
                },
    }
    return render(request, 'detail.html', context)
