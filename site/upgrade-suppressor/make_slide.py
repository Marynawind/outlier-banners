import cv2,numpy as np
a=cv2.imread('/Users/marynaradchuk/dev/фото/проэкт баннер/IMG_9666_fixed.jpg').astype(np.float32); H,W=a.shape[:2]
NH=int(round(W*9/16)); add=NH-H; top=add//2; bot=add-top
# top: the brick wall continues upward (mirror of the wall rows above the logo)
band=cv2.resize(a[1:171][::-1].copy(),(W,top),interpolation=cv2.INTER_LINEAR)
# the tall suppressor's top would be mirrored at x0..x1 -> replace with real brickwork from the wall to its left,
# its brightness bent to match both edges row by row
x0,x1=2520,2820; w=x1-x0
patch=band[:,x0-w:x0].copy()
lowp=cv2.GaussianBlur(patch,(0,0),25)
L=cv2.GaussianBlur(band[:,x0-12:x0],(0,0),6).mean(1); R=cv2.GaussianBlur(band[:,x1:x1+12],(0,0),6).mean(1)
t=np.linspace(0,1,w)[None,:,None]
target=L[:,None,:]*(1-t)+R[:,None,:]*t
patch=patch-lowp+target
k=np.zeros((top,W),np.float32); k[:,x0:x1]=1; k=cv2.GaussianBlur(k,(0,0),8)[...,None]
full=band.copy(); full[:,x0:x1]=patch
band=band*(1-k)+full*k
band*=np.linspace(0.75,1.0,top)[:,None,None]
# bottom: the dark front face of the table continues down and fades into darkness
b=cv2.resize(a[H-70:H],(W,bot+70),interpolation=cv2.INTER_LINEAR)[70:]*np.linspace(1.0,0.55,bot)[:,None,None]
b+=np.random.default_rng(1).normal(0,1.6,b.shape).astype(np.float32)
out=cv2.resize(np.vstack([band,a,b]),(1920,1080),interpolation=cv2.INTER_AREA)
cv2.imwrite('bd/upgrade-suppressor-1920x1080.jpg',np.clip(out,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,90])

# make room for the site's text box on the left: scene at 85%, aligned right; the dark wall/smoke continues around it
S=0.75; sw,sh=int(1920*S),int(1080*S); px,py=1920-sw,(1080-sh)//2
scene=cv2.resize(out,(sw,sh),interpolation=cv2.INTER_AREA)
pad=cv2.copyMakeBorder(scene,py,0,px,0,cv2.BORDER_REFLECT)                      # wall/smoke mirrored up and to the left
top_m=pad[:py].copy(); pad[:py]=cv2.GaussianBlur(top_m,(0,0),4)                  # softer, so no mirrored streaks read at the top
# below the table: a smooth dark gradient from the table's front face down to near black (no repeated edges)
lastrow=cv2.GaussianBlur(scene[-6:].mean(0,keepdims=True),(0,0),sigmaX=40,sigmaY=0)
lastrow=np.pad(lastrow,((0,0),(px,0),(0,0)),mode='edge')
nb=1080-sh-py; g=np.linspace(1.0,0.35,nb)[:,None,None]
below=lastrow*g+np.random.default_rng(2).normal(0,1.6,(nb,1920,3)).astype(np.float32)
pad=np.vstack([pad,below])
yy,xx=np.mgrid[0:1080,0:1920].astype(np.float32)
dx=np.clip((px-xx)/px,0,1); dy=np.maximum(np.clip((py-yy)/py,0,1),np.clip((yy-(py+sh))/(1080-sh-py),0,1))
dyt=np.clip((py-yy)/py,0,1)
fade=(1-0.55*dx)*(1-0.8*dyt)                      # the added margin sinks gently into darkness (like the photo's own vignette)
res=pad*fade[...,None]
inside=np.zeros((1080,1920),np.float32); inside[py:py+sh,px:]=1
k=cv2.GaussianBlur(inside,(0,0),10)[...,None]     # soft seam
res=res*(1-k)+pad*k
cv2.imwrite('bd/upgrade-suppressor-1920x1080.jpg',np.clip(res,0,255).astype(np.uint8),[cv2.IMWRITE_JPEG_QUALITY,90])
