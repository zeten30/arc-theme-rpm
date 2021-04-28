# RPM Makefile
FEDORA_RELEASE=34
VERSION=20210412

clean:
	rm -rf ./*.log
	rm -rf ./*.rpm
	rm -rf ./*.tar.xz

sources: clean
	curl https://github.com/jnsh/arc-theme/releases/download/$(VERSION)/arc-theme-$(VERSION).tar.xz -o ./arc-theme-$(VERSION).tar.xz

srpm: sources
	mock -r fedora-$(FEDORA_RELEASE)-x86_64 --spec arc-theme.spec --sources ./ --resultdir ./ --buildsrpm

rpm: srpm
	mock -r fedora-$(FEDORA_RELEASE)-x86_64 --rebuild arc-*.src.rpm --resultdir ./

copr: srpm 
	copr-cli build mzink/Utils rpmbuild/arc-*.src.rpm --nowait -r fedora-$(FEDORA_RELEASE)-x86_64 -r fedora-rawhide-x86_64
