Summary:	Screen recording tool based on mate desktop
Name:		mate-recorder
Version:	1.0.0
Release:	1
License:	GPLv3+ 
Group:		Graphical desktop/Other
URL:		https://github.com/zhuyaliang/mate-recorder
Source0:	https://github.com/zhuyaliang/mate-recorder/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		mate-recorder-1.0.0-use-ayatana-appindicator.patch
Patch1:		mate-recorder-1.0.0-fix_meson.patch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libwnck-3.0)

Suggests:	gstreamer1.0-plugins-ugly
Suggests:	x264

%description
Screen recording tool based on mate desktop.

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/screen-start.png
%{_datadir}/dbus-1/interfaces/org.screen.admin.xml
%{_metainfodir}/%{name}.appdata.xml

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson
%meson_build 

%install
%meson_install

desktop-file-install	\
	--delete-original \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# locales
%find_lang %{name} --with-gnome --all-name

