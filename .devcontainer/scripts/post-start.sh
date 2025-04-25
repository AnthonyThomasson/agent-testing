if command -v cursor &> /dev/null; then
    if [ -f ~/.zshrc ]; then
        echo "GIT_EDITOR=cursor" >> ~/.zshrc
    elif [ -f ~/.bashrc ]; then
        echo "GIT_EDITOR=cursor" >> ~/.bashrc
    else
        echo "GIT_EDITOR=cursor" >> ~/.profile
    fi
fi

if [ ! -f .env ] || ! grep -q "OPENAI_API_KEY" .env; then
    echo "OpenAI API key not found in .env file."
    echo "Please enter your OpenAI API key:"
    read -s api_key
    
    # Create or update .env file
    echo "OPENAI_API_KEY=$api_key" > .env
    echo "API key has been saved to .env file."
fi 

pip install -r requirements.txt
