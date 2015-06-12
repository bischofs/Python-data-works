
require 'mail'
require 'ntlm/smtp'


options = { :address              => "owa.fev-et.com",
  :port                 => 25,
  :domain               => 'fev.com',
  :user_name            => 'Icentral_Admin@fev.com',
  :password             => 'Podracer01',
  :authentication       => :login,
  :openssl_verify_mode  => 0
}



# Mail.defaults do
#   delivery_method :smtp, options
# end

Mail.defaults do
  delivery_method :smtp, options
end

$val = 36.5

Mail.deliver do
  to 'bischoff_s@fev.com'
  from 'icentraladmin@fev.com'
  subject 'Partical lab humidity out of range for 30 minutes'
  body "Last value recorded is #{$val}"
end
