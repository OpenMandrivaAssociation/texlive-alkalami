%global tl_name alkalami
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.000
Release:	%{tl_revision}.1
Summary:	A font for Arabic-based writing systems in Nigeria and Niger
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/alkalami
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alkalami.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alkalami.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This font is designed for Arabic-based writing systems in the Kano
region of Nigeria and Niger.

