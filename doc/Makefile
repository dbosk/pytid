.PHONY: all
all: nytid.pdf

LATEXFLAGS+=	-shell-escape
TEX_PYTHONTEX=	yes
PYTHONTEXFLAGS=	--interpreter "python:poetry run python3"

nytid.pdf: ../src/nytid/schedules.tex
nytid.pdf: ../src/nytid/signup/hr/hr.tex
nytid.pdf: ../src/nytid/signup/sheets.tex
nytid.pdf: ../src/nytid/signup/utils.tex

nytid.pdf: ../src/nytid/cli/init.tex

nytid.pdf: ../src/nytid

nytid.pdf: preamble.tex abstract.tex ../LICENSE

../src/nytid::
	${MAKE} -C $@ all

../%::
	${MAKE} -C $(dir $@) $(notdir $@)


.PHONY: clean
clean:
	${RM} nytid.pdf
	#${MAKE} -C ../src/nytid/cli clean
	${MAKE} -C ../src/nytid clean

.PHONY: distclean
distclean:
	${RM} -Rf __pycache__
	#${MAKE} -C ../src/nytid/cli distclean
	${MAKE} -C ../src/nytid distclean



INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
