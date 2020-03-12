# Base image for exposing port 5432
FROM jupyter/datascience-notebook
EXPOSE 5432
# docker run -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes --user root --name startups-jupyter -p 5432:5432 -v $(pwd):/home/jovyan/work -e PG_USER=sfs_db_user -e PG_PSWD=BEa*i^}97A$F,93@WN*9CDc2Xp6?9hCmQn+G?H23 jupyter/datascience-notebook
# docker run -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes --user root --name startups-jupyter -p 5432:5432 -v $(pwd):/home/jovyan/work -e PG_USER=sfs_db_user -e PG_PSWD=BEa*i^}97A$F,93@WN*9CDc2Xp6?9hCmQn+G?H23 roeeyn/my-nb