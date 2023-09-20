SUBDIR_GOALS=	all clean distclean

MODULES+=	__init__.py
MODULES+=	courses.py
MODULES+=	schedule.py
MODULES+=	signupsheets.py
MODULES+=	hr.py

EXTRAS+=	nytid.hourly.sh

.PHONY: all
all: ${MODULES} ${EXTRAS}

.INTERMEDIATE: init.py
__init__.py: init.py
	${MV} $< $@

nytid.hourly.sh: init.nw
	${NOTANGLE}

.PHONY: clean
clean:
	${RM} -R ${MODULES} __pycache__
	${RM} *.tex
	${RM} ${EXTRAS}


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/noweb.mk
include ${INCLUDE_MAKEFILES}/subdir.mk
