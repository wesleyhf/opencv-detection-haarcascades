import detector

# detector.image(
#     'files/faces.jpg',
#     'output/faces.jpg',
#     'haarcascades/frontalface_alt.xml',
#     1.3,
#     2
# );

# detector.image(
#     'files/faces2.png',
#     'output/faces2.png',
#     'haarcascades/frontalface_alt.xml',
#     1.2,
#     2
# );

detector.video(
    'files/chroma.avi',
    'output/chroma.avi',
    'haarcascades/frontalface_alt.xml',
);

# detector.video(
#     'files/walking.avi',
#     'output/walking.avi',
#     'haarcascades/fullbody.xml',
#     1.2,
#     5
# );

# detector.image(
#     'files/cars.jpg',
#     'output/cars.jpg',
#     'haarcascades/car.xml',
# );

# detector.video(
#     'files/cars1.avi',
#     'output/cars1.avi',
#     'haarcascades/car.xml',
# );

# detector.video(
#     'files/cars2.avi',
#     'output/cars2.avi',
#     'haarcascades/car.xml',
# );