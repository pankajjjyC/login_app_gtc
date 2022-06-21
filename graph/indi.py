import matplotlib.pyplot as plt
import base64
from io import BytesIO
def graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph
def plot(x,y):
    plt.switch_backend('AGG')#anti grain geometry
    plt.figure(figsize=(6,4))
    plt.title('Train Reservation')
    plt.plot(x,y)
    plt.xticks()
    plt.xlabel('Class')
    plt.ylabel('PNR_No')
    plt.tight_layout()
    get_graph=graph()
    return get_graph