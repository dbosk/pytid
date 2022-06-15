.PHONY: all
all: nytid.pdf

LATEXFLAGS+=	-shell-escape
TEX_PYTHONTEX=	yes

nytid.pdf: ../src/nytid/schedules/init.tex
nytid.pdf: ../src/nytid/schedules/utils.tex
nytid.pdf: ../src/nytid/cli/init.tex

nytid.pdf: preamble.tex abstract.tex ../LICENSE

../%::
	${MAKE} -C $(dir $@) $(notdir $@)


.PHONY: clean
clean:
	${RM} nytid.pdf
	${MAKE} -C ../src/nytid/cli clean
	${MAKE} -C ../src/nytid/schedules clean

.PHONY: distclean
distclean:
	${RM} -Rf __pycache__
	${MAKE} -C ../src/nytid/cli distclean
	${MAKE} -C ../src/nytid/schedules distclean



INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
