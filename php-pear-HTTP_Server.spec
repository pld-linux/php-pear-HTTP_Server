%include	/usr/lib/rpm/macros.php
%define         _class          HTTP
%define         _subclass       Server
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - HTTP server class
Summary(pl):	%{_pearname} - klasa do obs�ugi serwera HTTP
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9b900c74a641448b7b9b59fc1bfda4b6
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} class that allows you to easily implement HTTP servers by
supplying callbacks. The base class will parse the request, call the
apropriate callback and build a response based on an array that the
callbacks have to return.

This class has in PEAR status: %{_status}.

%description -l pl
...

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
