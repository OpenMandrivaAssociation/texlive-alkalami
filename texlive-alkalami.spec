Name:		texlive-alkalami
Version:	44497
Release:	2
Summary:	A font for Arabic-based writing systems in Nigeria and Niger
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/alkalami
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alkalami.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alkalami.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This font is designed for Arabic-based writing systems in the
Kano region of Nigeria and Niger.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/alkalami
%doc %{_texmfdistdir}/doc/fonts/alkalami

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
