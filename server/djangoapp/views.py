# Uncomment the required imports before adding the code
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments, post_review

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request


def logout_request(request):
    logout(request)
    data = {"userName": ""}  # Return empty username
    return JsonResponse(data)

# Create a `registration` view to handle sign up request


@csrf_exempt
def registration(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    user_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        user_exist = True
    except BaseException:
        logger.debug("{} is new user".format(username))
    if not user_exist:
        # Create user in auth_user table
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password)
        login(request, user)
        data = {"userName": username, "status": "Registered"}
    else:
        data = {"userName": "", "status": "User already exists"}
    return JsonResponse(data)


def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if (count == 0):
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name,
                     "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels": cars})

# Update the `get_dealerships` render list of dealerships all by default,
# particular state if state is passed


def get_dealerships(request, state="All"):
    if (state == "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/" + state
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})

# Create a `get_dealer_reviews` view to render the reviews of a dealer


def get_dealer_reviews(request, dealer_id):
    if request.method == "GET":
        endpoint = "/fetchReviews/dealer/" + str(dealer_id)
        reviews = get_request(endpoint)

        # Analyze sentiment for each review
        for review_detail in reviews:
            review_text = review_detail.get('review', '')
            # Call sentiment analyzer
            review_detail['sentiment'] = analyze_review_sentiments(review_text)

        return JsonResponse({"status": 200, "reviews": reviews})
# Create a `get_dealer_details` view to render the dealer details


def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        endpoint = "/fetchDealer/" + str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})

# Create a `add_review` view to submit a review


@csrf_exempt
def add_review(request):
    if not request.user.is_anonymous:
        data = json.loads(request.body)
        try:
            post_review(data)
            return JsonResponse({"status": 200})
        except BaseException:
            return JsonResponse(
                {"status": 401, "message": "Error in posting review"})
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})
