.PHONY: all
all: pytid.pdf

LATEXFLAGS+=	-shell-escape
TEX_PYTHONTEX=	yes

pytid.pdf: ../src/pytid/schedules/init.tex
pytid.pdf: ../src/pytid/schedules/utils.tex
pytid.pdf: ../src/pytid/cli/init.tex

pytid.pdf: preamble.tex abstract.tex ../LICENSE

../%::
	${MAKE} -C $(dir $@) $(notdir $@)


.PHONY: clean
clean:
	${RM} pytid.pdf
	${MAKE} -C ../src/pytid/cli clean
	${MAKE} -C ../src/pytid/schedules clean

.PHONY: distclean
distclean:
	${RM} -Rf __pycache__
	${MAKE} -C ../src/pytid/cli distclean
	${MAKE} -C ../src/pytid/schedules distclean



INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
