import cv2

def video(inputPath, outputPath, classifierPath, scale=1.1, minNeighbors=1, color=(0, 255, 255)):
    video = cv2.VideoCapture(inputPath)
    classifier = cv2.CascadeClassifier(classifierPath)

    codec = cv2.VideoWriter_fourcc('M' ,'J', 'P', 'G')
    fps = video.get(cv2.CAP_PROP_FPS)
    
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)

    output = cv2.VideoWriter(outputPath, codec, fps, size)

    while video.isOpened():
        ret, image = video.read()

        if ret == False: 
            break

        # if frame is None:
        #     break

        processImage(image, classifier, scale, minNeighbors, color)

        output.write(image)

    video.release()
    output.release()

def image(inputPath, outputPath, classifierPath, scale=1.1, minNeighbors=1, color=(0, 255, 255)):
    image = cv2.imread(inputPath)
    classifier = cv2.CascadeClassifier(classifierPath)

    processImage(image, classifier, scale, minNeighbors, color)

    cv2.imwrite(outputPath, image)

def processImage(image, classifier, scale, minNeighbors, color):
    objects = detect(image, classifier, scale, minNeighbors);

    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

def detect(image, classifier, scale, minNeighbors):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    return classifier.detectMultiScale(gray, scale, minNeighbors)