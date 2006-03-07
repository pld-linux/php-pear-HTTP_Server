%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Server
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - HTTP server class
Summary(pl):	%{_pearname} - klasa do obs³ugi serwera HTTP
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b1c05e2380d4b4c6d083f1740e512430
URL:		http://pear.php.net/package/HTTP_Server/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-HTTP
Requires:	php-pear-Net_Server >= 0.12.0
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} class that allows you to easily implement HTTP servers by
supplying callbacks. The base class will parse the request, call the
apropriate callback and build a response based on an array that the
callbacks have to return.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa HTTP_Server pozwala na ³atwe implementowanie serwerów HTTP
poprzez dostarczanie callbacków. Klasa bazowa analizuje ¿±danie,
wywo³uje odpowiedni callback i tworzy odpowied¼ w oparciu o tablicê
zwrócon± przez callback.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
