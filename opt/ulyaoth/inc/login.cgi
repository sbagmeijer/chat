#!/usr/bin/perl

require "$root/cgi/idle.cgi";

if($DATA{'n'} eq "" or length($DATA{'n'}) > 14 or $DATA{'n'} =~ /\./){

$loginerror = "";

content_type();
chat_login();

exit;

}


if($DATA{'id'}){

$loginerror = "*** IP relogin ($ENV{'REMOTE_ADDR'}). Please wait...";

$r = 1;

content_type();
chat_login();

exit;
}




opendir(RD, "$root/ops/ops/");

@files = readdir (RD);

      closedir(RD);

    foreach $entry (sort @files) {


        if ($entry ne '.' && $entry ne '..') {

                $entry =~ s/.db//;

               
if($DATA{'n'} =~ /$entry/i && $DATA{'n'} ne $entry && length($DATA{'n'}) == length($entry) && !-e "$root/ops/ops/$DATA{'n'}.db"){

$loginerror = "*** Sorry the nickname ! <b>$DATA{'n'}</b> or the password is not correct, please retype your nick and password and try to login again!";

content_type();
chat_login();

exit;


} 

}
}



if(-e "$root/online/users/$DATA{'n'}.db" && !-e "$root/ops/ops/$DATA{'n'}.db"){

$loginerror = "*** Sorry, nickname <b>$DATA{'n'}</b> is already in use, please choose another.";

content_type();
chat_login();

exit;

}


if(!-e "$root/ops/ops/$DATA{'n'}.db"){

require "$root/inc/loginuser.inc";

}elsif(-e "$root/ops/ops/$DATA{'n'}.db"){

require "$root/inc/loginops.inc";

}


if($DATA{'frames'} eq 'yes'){

$frames = "yes";

print "<HTML>\n";

print "<HEAD><title>$title</TITLE></HEAD>\n";

print "<FRAMESET ROWS=\"*,60\">\n";

print "<FRAME SRC=\"$location?n=$DATA{'n'}&room=$DATA{'room'}&id=$id#b\" name=\"display\" MARGINWIDTH=\"0\" MARGINHEIGHT=\"0\" FRAMEBORDER=\"NO\">\n";

print "<FRAME SRC=\"$location?n=$DATA{'n'}&room=$DATA{'room'}&id=$id&msg=/bottom\" name=\"message\" SCROLLING=\"no\" BORDERCOLOR=\"0000FF\" MARGINWIDTH=\"0\" MARGINHEIGHT=\"0\">\n";

print "</FRAMESET>\n\n</BODY>\n</HTML>\n";      

exit;


}else{


$room = $DATA{'room'};

$frames = "";

require "$root/inc/print_ann.inc";

exit;

}
