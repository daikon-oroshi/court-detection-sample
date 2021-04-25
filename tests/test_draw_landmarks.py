from matplotlib import pyplot as plt
import torchvision as tv
from court_detection.data.data_set import BdcDataSet
from court_detection.data.transforms import (Resize, RandomErasing)


class TestDrawLandmark(object):

    DIR_PATH = "../resources/image/court"

    def test_draw_landmark(self):
        size = (224, 224)
        transform = tv.transforms.Compose(
            [
                Resize(size),
                RandomErasing()
            ]
        )
        ds = BdcDataSet(self.DIR_PATH, transform=transform)
        for i in range(0, min(9, len(ds))):

            train_data = ds[i]
            for pt in train_data.landmarks:
                plt.plot(
                    size[0] * pt[0], size[1] * pt[1],
                    marker='x', color="red"
                )
            plt.imshow(train_data.image)
            plt.show()


if __name__ == "__main__":
    test = TestDrawLandmark()
    test.test_draw_landmark()