# Examination 7 - MariaDB installation

To make a dynamic web site, many use an SQL server to store the data for the web site.

[MariaDB](https://mariadb.org/) is an open-source relational SQL database that is good
to use for our purposes.

We can use a similar strategy as with the _nginx_ web server to install this
software onto the correct host(s). Create the playbook `07-mariadb.yml` with this content:

    ---
    - hosts: db
      become: true
      tasks:
        - name: Ensure MariaDB-server is installed.
          ansible.builtin.package:
            name: mariadb-server
            state: present

# QUESTION A

Make similar changes to this playbook that we did for the _nginx_ server, so that
the `mariadb` service starts automatically at boot, and is started when the playbook
is run.

- Jag la till att tjänsten ska startas automatiskt vid uppstart och startas direkt när playbooken körs genom att använda ansible.builtin.service med enabled: true och state: started.  

# QUESTION B

When you have run the playbook above successfully, how can you verify that the `mariadb`
service is started and is running?

- Jag verifierade att MariaDB körs genom att köra: 
ansible -i hosts -m shell -a "systemctl status mariadb" db

När jag såg redan Active: active (running) visste jag att tjänsten var igång. 

# BONUS QUESTION

How many different ways can use come up with to verify that the `mariadb` service is running?

- Jag kan verifiera att MariaDB körs på flera sätt: 
systemctl status mariadb
ps aux | grep mariadb 

eller via Ansible med samma kommandon som ovan. 