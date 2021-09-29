import csv, io
from re import S
from django.shortcuts import render
from django.contrib import messages
from .models import Profile
import logging
# Create your views here.
# one parameter named request
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = Profile.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    logger.debug(csv_file.name)
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            number = column[0],
            photoName = column[1],
            filter = column[2],
            shootingDate = column[3],
            shootinLocation = column[4],
            strain = column[5],
            width = column[6],
            height = column[7],
            camera = column[8],
            shootingTime = column[9],
            exposureTime = column[10],
            aperture = column[11],
            exposure = column[12],
            ISO = column[13],
            focalLength = column[14],
            filename = column[15],
            shootingArea = column[16],
            disease = column[17],
            plantsNumber = column[18],
            shootingFunction = column[19],
        )
    context={
       
    }
    
    return render(request, template, context)

    
# def singleVendor(request, id):
#     profile = Profile.objects.get(id = id)
#     context = {
#         'profile': profile
#     }
#     return render(request, 'profile_detail', context)
def singleVendor(request, id):
    profile = Profile.objects.get(id = id)
    context = {
        'profile': profile
    }
    return render(request, 'profile_detail.html', context)

def singleVendor2(request, id):
    logger.debug(request.method=="POST")
    profile = Profile.objects.get(id = id)
    context = {
        'profile': profile
    }
    if request.method == 'POST':
        logger.debug(request.POST['photoName'],request.POST['shootingDate'])
        Profile.objects.filter(id = id).update(
            number = request.POST['id'],
            filename = request.POST['filename'],
            photoName = request.POST['photoName'],
            filter = request.POST['filter'],
            shootingDate = request.POST['shootingDate'],
            shootinLocation = request.POST['shootinLocation'],
            strain = request.POST['width'],
            width = request.POST['height'],
            height = request.POST['strain'],
            camera = request.POST['camera'],
            shootingTime = request.POST['shootingTime'],
            exposureTime = request.POST['exposureTime'],
            aperture = request.POST['aperture'],
            exposure = request.POST['exposure'],
            ISO = request.POST['ISO'],
            focalLength = request.POST['focalLength'],
            disease = request.POST['disease'],
            plantsNumber = request.POST['plantsNumber'],
            shootingFunction = request.POST['shootingFunction'],
            )

        logger.debug(request.POST['photoName'])
        logger.debug(request.POST['shootingDate'])
    return render(request, 'profile_modify.html', context)

def display(request):
    profile = Profile.objects.filter(filename__contains="0312")
    context = {
        'profile': profile
    }
    return render(request, 'display.html', context)
