"""Tests for the file finder service."""

from atlanta_shore import file_finder_service


def test_is_present() -> None:
    """Confirm that the class and methods are present."""
    assert "FileFinderService" in dir(file_finder_service)
    assert "find_file_upwards" in dir(file_finder_service.FileFinderService)


def test_harness() -> None:
    """Test that the test harness is working."""
    file_finder = file_finder_service.FileFinderService()
    file_finder.find_file_upwards("crap.json")
    assert file_finder is not None


def test_file_found_immediately() -> None:
    """Test that the file finder service finds the file."""
    # ARRANGE
    filename = "setting.json"
    start_dir = "/home/user/project"

    def mock_isfile(path):
        return True  # because the test if for a file that exists.

    def mock_abspath(path):
        return path  # because we are starting with an absolute path.

    file_finder = file_finder_service.FileFinderService(
        isfile=mock_isfile, abspath=mock_abspath
    )
    # ACT
    result = file_finder.find_file_upwards(filename, start_dir)
    # ASSERT
    assert result == "/home/user/project/setting.json"


def test_file_found_in_parent_directory() -> None:
    """Test that the file finder service finds the file in the parent directory."""
    # ARRANGE
    filename = "setting.json"
    start_dir = "/home/user/project"

    def mock_isfile(path):
        """Find the file in the parent directory."""
        return path == "/home/user/setting.json"

    def mock_abspath(path):
        return path

    # ACT
    file_finder = file_finder_service.FileFinderService(
        isfile=mock_isfile, abspath=mock_abspath
    )
    result = file_finder.find_file_upwards(filename, start_dir)
    # ASSERT
    assert result == "/home/user/setting.json"


def test_file_finder_service_not_found() -> None:
    """Test that the file finder service does not find the file."""
    # ARRANGE
    filename = "non_existent_file.txt"
    start_dir = "/home/user/project"

    def mock_isfile(path):
        return False  # because the file must not be found.

    # ACT
    file_finder = file_finder_service.FileFinderService(isfile=mock_isfile)
    result = file_finder.find_file_upwards(filename, start_dir)
    # ASSERT
    assert result is None


def test_find_data_files() -> None:
    """Confirm that a sorted list of file paths is returned."""
    # ARRANGE
    pattern = "data-plant*.csv"

    def mock_glob(pathname, recursive):
        return [
            "/data/raw/2024-06/data-plant-2024-06.csv",
            "/data/raw/2019-02/data-plant-2019-02.csv",
        ]

    file_finder = file_finder_service.FileFinderService(glob=mock_glob)
    # ACT
    data_files = file_finder.find_data_files(pattern=pattern)
    # ASSERT
    assert len(data_files) == 2
    assert data_files[0].endswith("2019-02.csv")
