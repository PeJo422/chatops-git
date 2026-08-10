from chatops_git.cli import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "chatops-git is ready\n"
