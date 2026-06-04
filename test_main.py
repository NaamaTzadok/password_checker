from main import is_strong, main


def test_short_password():
    assert is_strong("123aN") is False


def test_no_capital_letters():
    assert is_strong("abcd1234") is False


def test_no_numbers_password():
    assert is_strong("abSMKOPNKNFk") is False


def test_strong_password():
    assert is_strong("StrongPassword10")


def test_main_with_week_password(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "123aN")
    main()
    capturd = capsys.readouterr()

    assert "Welcome to Password-Checker!" in capturd.out
    assert "Your password is weak." in capturd.out


def test_main_with_strong_password(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "StrongPassword10")
    main()
    capturd = capsys.readouterr()

    assert "Your password is strong." in capturd.out
