import matplotlib.pyplot as plt
import torchvision



def afficher_image(image):

    image = image.squeeze(0)  # Enlève la dimension de batch
    image = image.squeeze(0)  # Enlève la dimension du canal
        

    plt.imshow(image, cmap='gray')
    plt.axis('off')  # meilleure visibilité
    plt.show()

