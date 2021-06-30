Name:           fakechroot
Version:        2.19
Release:        9
Summary:        Gives a fake chroot environment
License:        LGPLv2+
URL:            https://github.com/dex4er/fakechroot
Source0:        https://github.com/dex4er/fakechroot/archive/%{version}/fakechroot-%{version}.tar.gz

Patch0000:      0001-Add-support-of-LFS-compatible-fts-functions.patch
Patch0001:      0002-fix-glic-2.33-_STAT_VER-not-defined.patch

Requires:       binutils binutils-devel
Provides:       fakechroot-libs = %{version}-%{release}
Obsoletes:      fakechroot-libs < %{version}-%{release}
BuildRequires:  autoconf automake libtool perl-podlators perl-generators

%description
fakechroot creates a fake environment in which user could run a command and
use the chroot(8) call without root privileges. This is useful when user want
a chrooted environment to install other packages without elevating privileges.

%package        help
Summary:        Documentation of fakechroot
%description    help
The documentation of fakechroot.

%prep
%autosetup -p1
chmod -x scripts/{relocatesymlinks,restoremode,savemode}.sh

%build
autoreconf -vfi
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
%delete_la

%check
#make check

%files
%doc scripts/{relocatesymlinks,restoremode,savemode}.sh
%license COPYING LICENSE
%{_bindir}/*fakechroot
%{_sbindir}/chroot.fakechroot
%config(noreplace) %{_sysconfdir}/fakechroot/*.env
%{_libdir}/fakechroot/

%files          help
%doc NEWS.md README.md THANKS.md
%{_mandir}/man1/fakechroot.1*

%changelog
* Wed Jun 30 2021 caodongxia<caodongxia@huawei.com> - 2.19-9
- Fix '_STAT_VER' undeclared

* Wed Jan 22 2020 gulining<gulining1@huawei.com> - 2.19-8
- Disable test

* Wed Nov 27 2019 lihao <lihao129@huawei.com> - 2.19-7
- Package Init

