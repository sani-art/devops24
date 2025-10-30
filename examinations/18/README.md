# Examination 18 - Write an Ansible module (VG)

Ansible modules are types of plugins that execute automation tasks on a 'target'. In the previous
examinations you have used many different modules, written by Ansible developers.

A module in Ansible is a Python script that adheres to a particular convention.

You can see the places where Ansible looks for modules by dumping the Ansible configuration
and then search for `DEFAULT_MODULE_PATH`:

    $ ansible-config dump | grep -i module_path

We will now write our own module, and run it through Ansible.

# QUESTION A

Look at [Developing modules](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)
and create a module that

* Is called `anagrammer`
* Takes one parameter, `message`, that is a string.
* Returns two values:
    - `original_message` that is the string that is passed through `message`
    - `reversed_message` that is the `message` string, only backwards (reversed).
* If the `original_message` and `reversed_message` is different, the `changed` parameter should be `True`, otherwise
  it should be `False`.

When you are done, you should be able to do

    $ ANSIBLE_LIBRARY=./library ansible -m anagrammer -a 'message="hello world"' localhost

And it should return

    localhost | CHANGED => {
        "changed": true,
        "original_message": "hello world",
        "reversed_message": "dlrow olleh"
    }

You should also be able to do

    ANSIBLE_LIBRARY=./library ansible -m anagrammer -a 'message="sirap i paris"' localhost

And it should return

    localhost | SUCCESS => {
        "changed": false,
        "original_message": "sirap i paris",
        "reversed_message": "sirap i paris"
    }

If you pass in 'fail me', it should fail like this:

    localhost | FAILED! => {
        "changed": true,
        "msg": "You requested this to fail",
        "original_message": "fail me",
        "reversed_message": "em liaf"
    }

# QUESTION B

Study the output of `ansible-config dump | grep -i module_path`. You will notice that there is a directory
in your home directory that Ansible looks for modules in.

Create that directory, and copy the Ansible module you just wrote there, then make a playbook
that uses this module with the correct parameters.

You don't need to worry about FQCN and namespaces in this examination.

# QUESTION C

Create a playbook called `18-anagrammer.yml` that uses this module.

Make the playbook use a default variable for the message that can be overriden by using something like:

    $ ansible-playbook --verbose --extra-vars message='"This is a whole other message"' 18-custom-module.yml

# BONUS QUESTION

What is the relationship between the booleans you can use in Python, and the various "truthy/falsy" values
you most often use in Ansible?

- I Python räknas vissa värden som falska (t.ex. False,0,None,"",{},[]),medan allt annat är sant(truthy).
Ansible bygger på Python men tolkar även YAML-värden som yes/no,on/off,true/false,1/0 på samma sätt. 

What modules/filters are there in Ansible that can safely test for "truthy/falsy" values, and return something
more stringent?

- För att testa sådana värden på ett säkert sätt kan man använda filter som:
. | bool-omvandlar värdet till True eller False
. | truthy och | falsy testar mer exakt vad som är sant och falskt.