DATADIR=~/walking

.PHONY: img
img:
	mkdir -p ${DATADIR}/img
	cd ${DATADIR} && \
	avconv -i orig.mp4 -ss 29 -t 5 img/output-%05d.png

.PHONY: download
download:
	mkdir ${DATADIR}
	cd ${DATADIR} && \
	youtube-dl https://www.youtube.com/watch?v=z1OKVC4VR04

.PHONY: scikit-image
scikit-image:
	pip install -U scikit-image
