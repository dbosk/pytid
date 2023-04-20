TARGETS=	nytid-storage.pdf

.PHONY: all
all: ${TARGETS}

nytid-storage.pdf: nytid-storage.svg

.PHONY: clean
clean:
	${RM} ${TARGETS}

.PHONY: distclean
distclean:

INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/doc.mk
