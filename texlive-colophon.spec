Name:		texlive-colophon
Version:	47913
Release:	1
Summary:	Provides commands for producing a colophon
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colophon
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colophon.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colophon.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colophon.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Colophons are a once-common design device by which a book (or
document) designer gave some information to his readers about
the design and makeup of the text. It typically includes the
publisher (if not included elsewhere in the document), font
size, leading size, measure, and of course font face
identification. Sometimes it includes information about the
tools used, as well. This package provides some highly
configurable macros, with sensible defaults, for producing
colophons without having to muck around with a lot of manual
code.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/colophon
%{_texmfdistdir}/tex/latex/colophon
%doc %{_texmfdistdir}/doc/latex/colophon

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
