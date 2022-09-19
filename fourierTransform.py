import cv2
import numpy as  np
import glob


def fastFourierTransform(image_path, display_output, parse_fft) :
    if parse_fft :
        list_images = glob.iglob("{}/*".format(image_path))
        for image_title in list_images:
            img = cv2.imread(image_title, cv2.IMREAD_GRAYSCALE)
            f = np.fft.fft2(img)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = 20 * np.log(np.abs(fshift))
            magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
            img_and_magnitude = np.concatenate((img, magnitude_spectrum), axis=1)
            if display_output :
                cv2.imshow(image_title, img_and_magnitude)
                
            cv2.waitKey(0)
            cv2.destroyAllWindows()


path = "letters"
fastFourierTransform(path, True, True)



    