from fourierTransform import fastFourierTransform


if __name__ == "__main__" :

    image_path = input("Enter the path of the images : ")
    try :
        if image_path == "Letter-Images" :
            fastFourierTransform(image_path, True, True)

        elif image_path == "Custom-Images" :
            fastFourierTransform(image_path, True, True)
        
        elif image_path == "Lines-Images" :
            fastFourierTransform(image_path, True, True)

    except KeyboardInterrupt :
        print("Code Exited -1")




