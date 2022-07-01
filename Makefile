SUBDIR_GOALS=all clean distclean

SUBDIR+=	src/nytid/schedules
SUBDIR+=	doc

version=$(shell sed -n 's/^ *version *= *\"\([^\"]\+\)\"/\1/p' pyproject.toml)

.PHONY: all publish

all:

publish: all
	poetry build
	poetry publish
	gh release create -t v${version} v${version} doc/nytid.pdf


.PHONY: clean distclean
clean:
distclean:
	${RM} -Rf dist

INCLUDE_MAKEFILES=makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
