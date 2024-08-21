.PHONY: clean clean-spec copr rpm sources spec srpm tests lint lint-cmt-msg lint-help-msg
.SILENT: help lint-cmt-msg lint-help-msg

DIST       ?= epel-7-x86_64
PROJECT    ?= cloudwatch-agent
PACKAGE    := $(PROJECT)
VERSION     = $(shell rpm -q --qf "%{version}\n" --specfile $(PACKAGE).spec | head -1)
RELEASE     = $(shell rpm -q --qf "%{release}\n" --specfile $(PACKAGE).spec | head -1)

GIT        := $(shell which git)
ASPELL     := $(shell which aspell)
RPMLINT    := $(shell which rpmlint)

ifdef GIT
HEAD_SHA := $(shell git rev-parse --short --verify HEAD)
TAG      := $(shell git show-ref --tags -d | grep $(HEAD_SHA) | \
                    git name-rev --tags --name-only $$(awk '{print $2}'))

BUILDID := %{nil}
ifndef TAG
BUILDID := .$(shell date --date="$$(git show -s --format=%ci $(HEAD_SHA))" '+%Y%m%d%H%M').git$(HEAD_SHA)
endif

spec: ## create spec file
	@git cat-file -p $(HEAD_SHA):$(PACKAGE).spec | sed -e 's,@BUILDID@,$(BUILDID),g' > $(PACKAGE).spec

sources: ## archive sources
sources: clean spec
	@git archive --format=tar --prefix=$(PROJECT)-$(VERSION)/ $(HEAD_SHA) | \
	     gzip > $(PROJECT)-$(VERSION).tar.gz

srpm: ## create srpm
srpm: sources
	@mkdir -p srpms/
	@rpmbuild -bs --define "_sourcedir $(CURDIR)" \
	          --define "_srcrpmdir $(CURDIR)/srpms" $(PACKAGE).spec

rpm: ## create rpm
rpm: srpm
	@mkdir -p rpms/$(DIST)
	/usr/bin/mock -r $(DIST) --resultdir rpms/$(DIST) \
	              --rebuild srpms/$(PACKAGE)-$(VERSION)-$(RELEASE).src.rpm

clean-spec:
	@git checkout $(PACKAGE).spec
endif

clean: ## clean build files
clean: clean-spec
	@rm -rf build dist srpms rpms $(PROJECT)-*.tar.gz
