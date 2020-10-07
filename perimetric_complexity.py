from scipy import ndimage
from scipy import misc

def perimetric_complexity(image_file):
    i=misc.imread(image_file,flatten=True)
    i=(i<0.5)+0 # Assumes 1-bit image
    area=sum(sum(i))
    fattened=i+ndimage.interpolation.shift(i,[0,1])+ndimage.interpolation.shift(i,[1,0])+ndimage.interpolation.shift(i,[1,1])+ndimage.interpolation.shift(i,[0,-1])+ndimage.interpolation.shift(i,[-1,0])+ndimage.interpolation.shift(i,[-1,-1])+ndimage.interpolation.shift(i,[-1,1])+ndimage.interpolation.shift(i,[1,-1])
    fattened=(fattened>0.5)+0
    edges=fattened-i
    thickened=edges+ndimage.interpolation.shift(edges,[0,1])+ndimage.interpolation.shift(edges,[1,0])+ndimage.interpolation.shift(edges,[0,-1])+ndimage.interpolation.shift(edges,[-1,0])
    thickened=(thickened>0.5)+0
    perimeter=sum(sum(thickened))/3.
    return perimeter*perimeter/area

def pelli (file1,file2):
    return abs(perimetric_complexity(file1)-perimetric_complexity(file2))


