require 'net/telnet'
require 'mail'
require 'ntlm/smtp'
require 'active_support/time'

def check()
  

  begin
    
    host = Net::Telnet::new("Host" => "172.26.16.150", "Prompt"=> /[>]\z/n)
    host.cmd("send")
    
    res = host.cmd("send")
    spl = res.split()
  
    $humid = spl.at(2).to_f
    $temp = spl.at(5).to_f
    $dew = spl.at(11).to_f
  
    if $humid > 50 or $humid < 40
      $hflag += 1 
    elsif $dew > 10.5 or $dew < 8.5
      $dflag += 1
    elsif $temp > 23.0 or $temp < 21.0
      $tflag += 1
    end

    host.close()

  rescue

    

  end

  
end

def report(flag)
  
  Mail.defaults do
    delivery_method :smtp, $options
  end

  if flag == "dew"
    Mail.deliver do
      to 'bischoff_S@fev.com'
      from 'icentraladmin@fev.com'
      subject 'Partical lab Dew Point out of range for 30 minutes'
      body "Last recorded value is #{$dew}"
    end
  elsif flag == "temp"
    Mail.deliver do
      to 'bischoff_S@fev.com'
      from 'icentraladmin@fev.com'
      subject 'Partical lab temperature out of range for 30 minutes'
      body "Last recorded value is #{$temp}"
    end
  elsif flag == "humid"
    Mail.deliver do
      to 'bischoff_S@fev.com'
      from 'icentraladmin@fev.com'
      subject 'Partical lab humidity out of range for 30 minutes'
      body "Last recorded value is #{$humid}"
    end
  end
  
end

$options = { :address              => "owa.fev-et.com",
  :port                 => 25,
  :domain               => 'fev.com',
  :user_name            => 'Icentral_Admin@fev.com',
  :password             => 'Podracer01',
  :authentication       => :login,
  :openssl_verify_mode  => 0
}

while(1)
  
  $hflag = $dflag = $tflag = 0
  
  check()

  if $tflag < 1 or $dflag < 1 or $hflag < 1 
    sleep(10.minutes)
    check()
    if $tflag < 2 or $dflag < 2 or $hflag < 2 
      sleep(10.minutes)
      check()
      if $tflag < 3 or $dflag < 3 or $hflag < 3 
        sleep(10.minutes)
        check()
        if $tflag < 4
          report("temp")
        elsif $dflag < 4 
          report("dew")
        elsif $hflag < 4
          report("humid")
        end
      end
    end
  end
  

  sleep(5.minutes)
  
end

