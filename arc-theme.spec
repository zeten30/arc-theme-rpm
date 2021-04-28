%global common_desc       \
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and \
Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments \
like Gnome, Cinnamon, Budgie, Pantheon, XFCE, Mate, etc.

Name: arc-theme
Version: 20210412
Release: 3%{?dist}
Summary: Flat theme with transparent elements (git master snapshot)

License: GPLv3+
URL: https://github.com/jnsh/%{name}
Source0: https://github.com/jnsh/arc-theme/releases/download/%{version}/arc-theme-%{version}.tar.xz

BuildArch: noarch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cinnamon
BuildRequires: fdupes
BuildRequires: gtk-murrine-engine
BuildRequires: gtk3-devel
BuildRequires: inkscape
BuildRequires: meson
BuildRequires: optipng
BuildRequires: sassc

Requires: filesystem
Requires: gnome-themes-standard
Requires: gtk-murrine-engine

%description
%{common_desc}

%prep
%autosetup

%build
%meson -Dthemes=gnome-shell,gtk2,gtk3,metacity,plank,xfwm -Dgnome_shell_version=40
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*

%changelog
* Wed Apr 28 2021 Milan Zink <zeten30@gmail.com> - 20210428-2
- Initial RPM build using github master branch
