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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This font is designed for Arabic-based writing systems in the Kano
region of Nigeria and Niger.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/doc/fonts/alkalami
%dir %{_datadir}/texmf-dist/fonts/truetype/public
%dir %{_datadir}/texmf-dist/fonts/truetype/public/alkalami
%doc %{_datadir}/texmf-dist/doc/fonts/alkalami/AlkalamiSample.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/alkalami/AlkalamiSample.tex
%doc %{_datadir}/texmf-dist/doc/fonts/alkalami/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/alkalami/README.TEXLIVE
%doc %{_datadir}/texmf-dist/doc/fonts/alkalami/README.txt
%{_datadir}/texmf-dist/fonts/truetype/public/alkalami/Alkalami-Light.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/alkalami/Alkalami-Regular.ttf
