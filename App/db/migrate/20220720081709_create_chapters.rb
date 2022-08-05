class CreateChapters < ActiveRecord::Migration[6.1]
  def change
    create_table :chapters do |t|
      t.string :revelation_place
      t.string :name
      t.integer :chapter_number

      t.timestamps
    end
  end
end
