from main import check_password_strength, main


def test_short_password():
    assert check_password_strength("123aN") == 3


def test_no_capital_letters():
    assert check_password_strength("abcd1234") == 3


def test_no_numbers_password():
    assert check_password_strength("abSMKOPNKNFk") == 3


def test_no_lower_case_letters():
    assert check_password_strength("NOLOWERCASELETTERS10") == 3


def test_strong_password():
    assert check_password_strength("StrongPassword10") == 4


def test_main_super_weak_password(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "")
    main()
    capturd = capsys.readouterr()

    assert "Welcome to Password-Checker!" in capturd.out
    assert "Strenth Level: Super Weak 🥶" in capturd.out


def test_main_very_weak_password(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    main()
    capturd = capsys.readouterr()

    assert "Welcome to Password-Checker!" in capturd.out
    assert "Strenth Level: Very Weak ⚠️" in capturd.out


def test_main_weak_password(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1a")
    main()
    capturd = capsys.readouterr()

    assert "Welcome to Password-Checker!" in capturd.out
    assert "Strenth Level: Weak 👎🏽" in capturd.out


def test_main_medium_password(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1aB")
    main()
    capturd = capsys.readouterr()

    assert "Welcome to Password-Checker!" in capturd.out
    assert "Strenth Level: Medium 👍🏽" in capturd.out


def test_main_strong_password(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1234AbCdEfG")
    main()
    capturd = capsys.readouterr()

    assert "Welcome to Password-Checker!" in capturd.out
    assert "Strenth Level: Strong 💪🏽" in capturd.out
