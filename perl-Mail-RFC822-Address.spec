#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Mail
%define		pnam	RFC822-Address
%include	/usr/lib/rpm/macros.perl
Summary:	Mail::RFC822::Address - validating email addresses according to RFC822
Summary(pl.UTF-8):	Mail::RFC822::Address - sprawdzanie poprawności adresów e-mail wg RFC822
Name:		perl-Mail-RFC822-Address
Version:	0.3
Release:	2
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0bd88b2ffedd95a4a920053fd6d0b709
URL:		http://search.cpan.org/dist/Mail-RFC822-Address/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::RFC822::Address validates email addresses against the grammar
described in RFC 822 using regular expressions. How to validate a user
supplied email address is a FAQ (see perlfaq9): the only sure way to
see if a supplied email address is genuine is to send an email to it
and see if the user recieves it. The one useful check that can be
performed on an address is to check that the email address is
syntactically valid. That is what this module does.

This module is functionally equivalent to RFC::RFC822::Address, but
uses regular expressions rather than the Parse::RecDescent parser.
This means that startup time is greatly reduced making it suitable for
use in transient scripts such as CGI scripts.

%description -l pl.UTF-8
Mail::RFC822::Address sprawdza poprawność adresów e-mail wg gramatyki
opisanej w RFC 822 przy użyciu wyrażeń regularnych. Sposób sprawdzenia
poprawności adresu e-mail podanego przez użytkownika jest w FAQ
(perlfaq9): jedynym sposobem sprawdzenia, czy podany adres jest
prawdziwy jest wysłanie na niego wiadomości i sprawdzenie, czy
użytkownik ją otrzyma. Jedyny użyteczny test który można wykonać na
adresie to sprawdzenie, czy adres jest poprawny syntaktycznie - i to
właśnie robi moduł.

Ten moduł jest funkcjonalnie równoważny RFC::RFC822::Address, ale
używa wyrażeń regularnych zamiast analizatora Parse::RecDescent.
Oznacza to znaczne zmniejszenie czasu ładowania, co czyni moduł
przydatnym do używania w skryptach np. CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Mail/RFC822
%{_mandir}/man3/*
