%global debug_package %{nil}

Name:		lib{{{ git_dir_name }}}
Version:	{{{ git_dir_version }}}
Release:	1%{?dist}
Summary:	Apple Lossless Codec

License:	Apache License 2.0
URL:		http://alac.macosforge.org/
VCS:		{{{ git_dir_vcs }}}

Source:		{{{ git_dir_pack }}}

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and supported on iPhone, iPad, most iPods, Mac and iTunes. ALAC is a data compression method which reduces the size of audio files with no loss of information. A decoded ALAC stream is bit-for-bit identical to the original uncompressed audio file.

%package	devel
Summary:	Development package for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Files for development with %{name}.

%package	tools
Summary:	Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description	tools
Command line tool alacconvert that accepts CAF/WAVE files containing pcm data for encoding ALAC into a CAF file. It accepts CAF files containing ALAC for decoding to pcm in CAF/WAVE files. 

%prep
{{{ git_dir_setup_macro }}}

%build
# Rename README.md to README for automake
mv README.md README
autoreconf -fi
%configure --enable-example
%make_build

%install
%make_install

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}.*a
%{_libdir}/pkgconfig/alac.pc
%{_includedir}/alac/*

%files tools
%{_bindir}/alacconvert

%changelog
%autochangelog
