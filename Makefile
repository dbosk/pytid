SUBDIR_GOALS=all

SUBDIR+=	src/pytid/schedules

.PHONY: all publish

all:
publish: all
	poetry build
	poetry publish


.PHONY: clean
clean:
	${RM} -Rf dist

INCLUDE_MAKEFILES=makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
