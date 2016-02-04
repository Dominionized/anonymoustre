@echo off
git add -A
git commit
git push
git subtree push --prefix public origin gh-pages