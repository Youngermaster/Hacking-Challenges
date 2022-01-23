# -sCV gets the version and the services that runs on the given ports.
# -p$(ports) The given ports.

nmap -sCV -p$(ports) $ip
