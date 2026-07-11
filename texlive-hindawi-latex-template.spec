%global tl_name hindawi-latex-template
%global tl_revision 57757

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A LaTeX template for authors of the Hindawi journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hindawi-latex-template
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hindawi-latex-template.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hindawi-latex-template.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains a LaTeX template for authors of the Hindawi
journals. Authors can use this template for formatting their research
articles for submissions. The package has been created and is maintained
by the Typeset team.

