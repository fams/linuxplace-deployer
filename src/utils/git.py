from utils.utils import *

def git_pull(branch="master"):
	command(f"git pull origin {branch}")

def fetch_repo(repo, path, branch="master"):
	alert(f"# Clonando repo {repo} em {path}")
	if there_is_dir(path):
		old_path = pwd()
		chdir(path, imprime=False)
		git_pull()
		chdir(old_path, imprime=False)
	else:
		cmd = f"git clone {repo} -b {branch} {path}"
		command(cmd)

def get_last_tag():
	null, out = command(f"git describe --abbrev=0 --tag")
	return out

def there_is_modification():
	# esse comando lista alteracoes em arquivos, caso exista retorna sim
	null, out = command(f"git status --porcelain")
	alert(f"# Arquivos alterados:\n{out}")
	if out:
		return True
	else:
		return False

def git_add_all():
	command(f"git add -A")

def git_commit_and_push(msg, branch="master"):
	# TODO tirar o echo
	print(f"echo git commit -m {msg};echo git push origin {branch}")

def add_and_push(branch="master"):
	#alert(f"# Ultima tag da branch {branch}: {get_last_tag()}")
	if there_is_modification():
		alert("# Repositorio com atualizacoes")
		git_add_all()
		git_commit_and_push(f"Deploy ArgoCD APP	")
		alert(f"# Commit e Push feitos para origin {branch}")
	else:
		alert("# Nao existe modificacoes e por isso nao exige acoes nesse repositorio")
		return

# TODO POC
class Git:
	last_tag = ""
	last_commit = ""

	def __init__(self):
		self.last_tag = self.get_last_tag()

	#git add
	#if [ -n "$(git status -uno --porcelain)" ]; then git add -A && git commit -m "Deploy ${release_name}" && git push origin master; else echo "Nada a commitar!"; fi

	#git new tag


	#git get last tag
	def get_last_tag(self):
		null, out = command(f"git describe --abbrev=0 --tag")
		return out


#git push