QCHECKSTYLE=go run $(QBOXROOT)/base/qiniu/src/github.com/qiniu/checkstyle/gocheckstyle/*.go -config=.qcodestyle
QCOV=go run $(QBOXROOT)/base/com/src/github.com/axw/gocov/gocov/*.go
QCOVHTM=go run $(QBOXROOT)/base/com/src/github.com/matm/gocov-html/*.go -n

all:
	make install

fusion:
	cd src/qiniu.com/fusionsophon/fusion.v2; go install -v ./...

# make specific fusion service with:
# `make service SVC=fusionsslcert`
service:

	go install qiniu.com/fusionsophon/fusion.v2/$(SVC)/...

domainunifymgr:
	cd src/qiniu.com/fusionsophon/domainunify; go install -v ./...

install:
	cd src/qiniu.com; go install -v ./...

coverage:
	cd src; curl https://aone.qiniu.io/api/coverage/collect?token=A59B8029-E9A1-4FF3-B72B-3657CEAC64D4 | bash

clean:
	cd src/qiniu.com; go clean -i ./...

style:
	@$(QCHECKSTYLE) src

format:
	find ./ -name "*.go"|egrep -v '\/vendor\/|_test.go' |xargs gofmt -s -w

