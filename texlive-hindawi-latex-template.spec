Name:		texlive-hindawi-latex-template
Version:	57757
Release:	1
Summary:	A LaTeX template for authors of the Hindawi journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hindawi-latex-template
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hindawi-latex-template.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hindawi-latex-template.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains a LaTeX template for authors of the
Hindawi journals. Authors can use this template for formatting
their research articles for submissions. The package has been
created and is maintained by the Typeset team.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/hindawi-latex-template

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
